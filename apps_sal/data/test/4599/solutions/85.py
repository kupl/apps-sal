n = int(input())
n_list = list(map(int, input().split()))
alice = []
bob = []
while(n_list != []):
    a = max(n_list)
    alice.append(a)
    n_list.remove(a)
    if(n_list == []):
        break
    b = max(n_list)
    bob.append(b)
    n_list.remove(b)
print(sum(alice) - sum(bob))
