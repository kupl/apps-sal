from sys import stdin,stdout

n,m=stdin.readline().strip().split(' ')
n,m=int(n),int(m)

row=list(map(int,stdin.readline().strip().split(' ')))
col=list(map(int,stdin.readline().strip().split(' ')))
x=int(stdin.readline().strip())

lowest_row_array=[0]
for i in range(1,n+1):
    s=sum(row[:i])
    j=i
    min_till_now=s
    while j<n:
        s=s-row[j-i]+row[j]
        if s<min_till_now:
            min_till_now=s
        j+=1
    lowest_row_array.append(min_till_now)

lowest_col_array=[0]
for i in range(1,m+1):
    s=sum(col[:i]);
    j=i
    min_till_now=s
    while j<m:
        s=s-col[j-i]+col[j]
        if s<min_till_now:
            min_till_now=s
        j+=1
    lowest_col_array.append(min_till_now)
max_size=0;
if len(lowest_col_array)==1:
    lowest_col_array[0]=1
if len(lowest_row_array)==1:
    lowest_row_array[0]=1

for i in range(len(lowest_row_array)):
    for j in range(len(lowest_col_array)):
        if lowest_row_array[i]*lowest_col_array[j]<=x:
            if i*j>max_size:
                max_size=i*j

# print(lowest_col_array)
# print(lowest_row_array)
print(max_size)

