f = lambda: list(map(int, input().split()))

n, k = f()

t = list(f())



d = {0: 0}

for q in t:

    for i in range(1, k + 1): d[q * i] = i



for j in range(int(input())):

    a = int(input())

    p = [i + d[a - b] for b, i in list(d.items()) if a - b in d]

    print(min(p) if p and min(p) <= k else -1)




# Made By Mostafa_Khaled

