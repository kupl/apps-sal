k = int(input())

def snuke(n):
    def func(a):
        s = 0
        for i in str(a):
            s += int(i)
        return a/s
    
    len_n = len(str(n))
    min_snu = 10 ** 100
    for i in range(len_n):
        snu = str(n)[:len_n-i] + i * '9'
        func_snu = func(int(snu))
        if min_snu > func_snu:
            min_snu = func_snu
            snukee = int(snu)
            
    return snukee

count = 0
n = 1
while count < k:
    next_snuke = snuke(n)
    print(next_snuke)
    n = next_snuke + 1
    count += 1
