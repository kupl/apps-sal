class PalArray():
    P = 998244353
    def __init__(self, n, k, a):
        self.n, self.k, self.a = n, k, a
        self.dp = None

    def fast_pow(self, a, b):
        r = 1
        while b > 0:
            if b%2 == 1:
                r = (r*a)%self.P
            a = (a*a)%self.P
            b = int(b/2)
        return r

    def populate_dp(self):
        self.dp = [[0 for i in range(2)] for j in range(self.n+1)]
        self.dp[1][0] = self.k-2
        self.dp[1][1] = self.k-1

        for i in range(2, self.n+1):
            self.dp[i][0] = (((self.k-2)*(self.dp[i-1][0]))%self.P + self.dp[i-1][1])%self.P
            self.dp[i][1] = ((self.k-1)*self.dp[i-1][0])%self.P

    def check_array(self, a):
        for i in range(1, len(a)):
            if a[i] != -1 and a[i] == a[i-1]:
                return False
        return True

    def compute_count(self, a):
        check = False
        res = 1
        mis_cnt = 0
        lv = None
        for v in a:
            if v == -1:
                mis_cnt += 1
            else:
                if mis_cnt > 0:
                    if not check:
                        check = True
                        res = (res*self.fast_pow(self.k-1, mis_cnt))%self.P
                    else:
                        res = (res*self.dp[mis_cnt][int(lv==v)])%self.P
                    mis_cnt = 0
                lv = v
                check = True
        if mis_cnt > 0:
            if lv is not None:
                res = (res*self.fast_pow(self.k-1, mis_cnt))%self.P
            else:
                res = (((res*self.fast_pow(self.k-1, mis_cnt-1))%self.P)*self.k)%self.P
        return res

    def num_combinations(self):
        self.populate_dp()
        a1 = [self.a[i] for i in range(0,self.n,2)]
        a2 = [self.a[i] for i in range(1,self.n,2)]
        cnt1 = self.compute_count(a1)*int(self.check_array(a1))
        cnt2 = self.compute_count(a2)*int(self.check_array(a2))
        return (cnt1*cnt2)%self.P

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
print(PalArray(n,k,a).num_combinations())




