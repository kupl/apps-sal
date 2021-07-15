def my_input():
    return list(map(int,input().split()))

n,_= my_input()
ans = n-sum(my_input())
print((ans if ans>=0 else -1))

