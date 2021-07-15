t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    for i in range(4*10**5):
        if (i*(i+1)//2 + a + b) % 2 == 0:
            if (i*(i+1))//2 >= abs(a-b):
                print(i)
                break

