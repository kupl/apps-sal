n, k = list(map(int, input().split()))
new_dict = {}
t = input()
for x in t:
    if x in new_dict:
        new_dict[x] = new_dict[x] + 1
    else:
        new_dict[x] = 1

p = 0

# print(new_dict.items())

while(k > 0):
    if(new_dict[max(new_dict, key=new_dict.get)] >= k):
        p = p + k**2
        k = 0
    else:
        p = p + new_dict[max(new_dict, key=new_dict.get)]**2
        k = k - new_dict[max(new_dict, key=new_dict.get)]
        del new_dict[max(new_dict, key=new_dict.get)]
    #	print("hello\n")
print(p)
