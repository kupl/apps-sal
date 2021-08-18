class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0] * k
        for num in arr:
            count[num % k] += 1

        print(count)
        for x in range(k):
            comp = -x % k
            print(comp)
            while count[x] > 0:
                count[x] -= 1
                count[comp] -= 1
                if count[comp] < 0:
                    return False

        return True
