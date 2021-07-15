N = int(input())
data = list(map(int,input().split()))

data_2 =(max(data) < (sum(data)-max(data)))

if data_2:
    print("Yes")
else:
    print("No")
