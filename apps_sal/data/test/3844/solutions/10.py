n = int(input())
l = list(map(int, input().split()))
l1 = [0] * (max(l) + 1)
for i in range(n):
    l1[l[i]] += 1
for elem in l1:
    if elem % 2 == 1:
        print('Conan')
        break
else:
    print('Agasa')
