(a, b) = list(map(int, input().split()));
if(b - a >= 10):
    print((0));
    return;
else:
    x = 1;
    for i in range(a + 1, b + 1):
        x = (x * (i % 10)) % 10;
print(x);
