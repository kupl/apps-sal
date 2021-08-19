a = input()
b = int(input())
j = 0
l = 0
for start in range(len(a) + b):
    for end in range(start + 1, len(a) + b):
        if (end - start + 1) % 2 == 0:
            middle = (start + end) // 2 + 1
            k = 0
            for traverse in range(start, len(a)):
                if k + middle >= len(a) or k + middle > end:
                    j = end - start + 1
                    if j > l:
                        l = j
                elif k + middle < len(a) and a[traverse] != a[middle + k]:
                    break
                elif k + middle < len(a) and a[traverse] == a[middle + k]:
                    k += 1
print(l)
