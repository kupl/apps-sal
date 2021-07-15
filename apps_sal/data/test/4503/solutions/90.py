# B - Common Raccoon vs Monster

# H N
H, N = list(map(int, input().split()))
my_list = list(map(int, input().split(maxsplit=N)))

if H <= sum(my_list):
    answer = 'Yes'
else:
    answer = 'No'

print(answer)

