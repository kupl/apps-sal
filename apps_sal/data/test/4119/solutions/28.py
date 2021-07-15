def main():
    n,m = list(map(int, input().split()))
    pos_list = list(map(int, input().split()))
    pos_list.sort()

    if n >= m:
        return 0
    diff_list =[0]
    for i in range(m-1):
        diff_list.append(pos_list[i+1]-pos_list[i])
    diff_list.sort()
    #print(pos_list)
    #print(diff_list)
    if n==1:
        return sum(diff_list)
    return sum(diff_list[:-n+1])

print(main())
