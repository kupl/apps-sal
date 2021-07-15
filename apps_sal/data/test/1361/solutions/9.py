holds= int(input())
heights= [int(i) for i in input().split()]
ans= 999999999
real= heights
for i in range(1, len(heights)-1):
    #print(i, heights, real)
    app= heights[i]
    heights.remove(app)
    k= 0
    for j in range(len(heights)-1):
        k= max(heights[j+1]-heights[j], k)
    
    ans= min(ans, k)
    heights.append(app)
    heights= sorted(heights)
    
print(ans)
