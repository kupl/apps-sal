r, c = list(map(int, input().split()))
ip = []
for i in range(r):
    ip += list(input().split())

if 'C' in ip or 'Y' in ip or 'M' in ip:
    print('#Color')
else:
    print('#Black&White')
