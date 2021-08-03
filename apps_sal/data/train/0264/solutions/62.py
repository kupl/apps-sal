class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr.sort()
        self.arr = arr
        self.tmp = []
        self.mlen = 0
        self.len = 0
        self.backtrack(0)
        return self.mlen

    def backtrack(self, pos):
        # print(self.tmp,self.len)
        if pos == len(self.arr):

            if self.len > self.mlen:
                # print(self.len,self.mlen)
                self.mlen = self.len
            return
        lb = len(self.tmp)
        self.tmp = self.tmp + list(self.arr[pos])
        l = len(self.arr[pos])
        if l == len(self.arr[pos]) and lb + l == len(set(self.tmp)):

            self.len += l
            self.backtrack(pos + 1)
            self.len -= l

        # for i in range(l):
        #     self.tmp.pop()
        self.tmp = self.tmp[:-l]
        self.backtrack(pos + 1)
