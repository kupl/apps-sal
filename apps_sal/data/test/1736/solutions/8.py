inp1,inp2 = [int(i) for i in input().split(" ")],[int(i) for i in input().split(" ")]
max = right = result = 0
l = len(inp2)
for i in range(0,l):
    if max < len(inp2):
        while right < l and result + inp2[right] <= inp1[1]:
            result+=inp2[right]
            right+=1
        if max < right - i:
            max = right - i
        result-= inp2[i]
    else:
        print(max)
        return
print(max)
