
r, g, b = list(map(int, input().split()))
a = r // 3 + g // 3 + b // 3 + min(r % 3, g % 3, b % 3)

n = [r, g, b]

for i in range(3):
    w = True
    for j in range(3):
        if(i != j):
            if(n[j] % 3 != 2):
                w = False
    if(w and n[i] % 3 == 0 and n[i] >= 3):
        a += 1
print(a)
