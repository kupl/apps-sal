n = int(input())
stol = [0 for i in range(n)]
a = input().split()
m = 0
k = 0
for e in a:
    if stol[int(e) - 1] == 0:
        stol[int(e) - 1] = 1
        k += 1
        if k > m:
            m = k
    else:
        stol[int(e) - 1] = 0
        k -= 1
print(m)
