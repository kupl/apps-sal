N = int(input())
N_List = list(map(int, input().split()))
maxN = max(N_List)
print(('No', 'Yes')[sum(N_List) - maxN > maxN])
