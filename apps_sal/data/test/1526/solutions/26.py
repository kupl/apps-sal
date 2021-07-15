num = list(map(int,input().split()))
numSort=sorted(num)

count=numSort[2]-numSort[1]
count+=(numSort[2]-(numSort[0]+count))/2
count=int(count) if count.is_integer() else int(count+1.5)

print(count)

