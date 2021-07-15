

n, k = list(map(int, input().split()))

t = list(map(int, input().split()))

print(min((sum(t[i :: k]), i) for i in range(k))[1] + 1)



# Made By Mostafa_Khaled

