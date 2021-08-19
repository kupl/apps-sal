"""  if need to find numbers 1...n such that n% (|i-j|>1)>0, can solv as p^k, p is prim num & answr or belw process"""
while True:
    try:
        n = int(input())
        (num, i) = ([], 2)
        if n == 1:
            print('1')
            continue
        while i * i <= n:
            if n % i == 0:
                num.append(i)
                while n % i == 0:
                    n /= i
            i += 1
        if n > 1:
            num.append(n)
        if len(num) > 1:
            print(1)
        else:
            print(num[0])
    except EOFError:
        break
