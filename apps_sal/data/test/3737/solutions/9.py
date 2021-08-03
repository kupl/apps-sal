input()
a = list(map(int, input().split()))
mi = min(a)
ma = max(a)
ch = 0
for i in range(len(a)):
    if a[i] != mi and a[i] != ma:
        ch += 1
print(ch)
