(n, m) = [int(i) for i in input().split()]
for i in range(n):
    s = input().split()
    if 'Y' in s or 'C' in s or 'M' in s:
        print('#Color')
        break
else:
    print('#Black&White')
