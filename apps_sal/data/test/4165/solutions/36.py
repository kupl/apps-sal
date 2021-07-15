n=int(input())
l_list=[int(i) for i in input().split()]

if max(l_list)<sum(l_list)-max(l_list):
    print("Yes")
    
else:
    print("No")
