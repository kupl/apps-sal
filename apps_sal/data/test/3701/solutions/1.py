n, x, y = map(int, input().split());
s = input()
ne = 0;
count = 0;
for i in range(1, n + 1):
    if (s[i - 1]  == '0'):
        count += 1;
    if (s[i - 1] == '1' or (s[i - 1] == '0' and i > 1 and s[i - 2] == '0')):
        p = ne;
    elif count == 1:
        ne += y;
        
    else:
        ne += min(x, y);
print(ne)
