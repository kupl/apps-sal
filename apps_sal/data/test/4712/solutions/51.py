HW = input().split()

H = int(HW[0])
W = int(HW[1])

lst = []

for i in range(H):
    lst.append('#' + input() + '#')

print('#' * (W + 2))

for s in lst:
    print(s)

print('#' * (W + 2))
