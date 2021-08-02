from math import gcd


class Factor:
    def __init__(self, max_element):
        self.minFactor = [-1] * (max_element + 1)
        for i in range(2, max_element + 1):
            if self.minFactor[i] == -1:
                for j in range(i, max_element + 1, i):
                    self.minFactor[j] = i

    def getFactorSet(self, element):
        retSet = set(1)
        while element > 1:
            retSet.add(element)
            retSet.add(self.minFactor[element])
            element //= self.minFactor[element]
        return retSet

    def getPrimeFactorSet(self, element):
        retSet = set()
        while element > 1:
            retSet.add(self.minFactor[element])
            element //= self.minFactor[element]
        return retSet

    def getPrimeFactorDic(self, element):
        retDic = {}
        while element > 1:
            val = self.minFactor[element]
            if val in retDic:
                retDic[val] += 1
            else:
                retDic[val] = 1
            element //= val
        return retDic


def main():
    n = int(input())
    a = list(map(int, input().split()))
    f = True
    fact = Factor(max(a))
    st = set()
    for v in a:
        fac_set = fact.getPrimeFactorSet(v)
        for u in fac_set:
            if u in st:
                f = False
                break
            st.add(u)
        if not f:
            break
    if f:
        print("pairwise coprime")
    else:
        all_gcd = a[0]
        for i in range(1, n):
            all_gcd = gcd(all_gcd, a[i])
        if all_gcd == 1:
            print("setwise coprime")
        else:
            print("not coprime")


def __starting_point():
    main()


__starting_point()
