n, m = map(int, input().split())
fl = False
for i in range(n):
    line = input()
    if 'C' in line or 'M' in line or 'Y' in line:
        fl = True
if fl:
    print('#Color')
else:
    print('#Black&White')
