n = int(input())
mas = list(map(int, input().split()))
m = mas[0]
count = 1
mm = []
for i in range(n):
    if mas[i] > m:
        m = mas[i]
        count += 1
    else:
        mm.append(count)
        count = 1
        m = mas[i]
mm.append(count)
print(max(mm))
