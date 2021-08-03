n = int(input())
bool = False
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            bool = True
if bool:
    print('Yes')
else:
    print('No')
