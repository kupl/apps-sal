S_list = list(map(int,input().split()))
sum_bell=sum(S_list)
hantei = list()
for i in S_list:
    hantei.append(sum_bell - i)
print(min(hantei))
