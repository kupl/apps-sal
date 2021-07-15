N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))
odd_count = 0
for a in A:
    if a % 2 == 0:
        print(a//2)
    else:
        if odd_count % 2 == 0:
            print((a+1)//2)
        else:
            print((a-1)//2)
        odd_count+=1




