n, m = list(map(int, input().split()))
x, k, y= list(map(int, input().split()))
start_ls = list(map(int, input().split()))
end_ls = list(map(int, input().split()))

len_start_ls = len(start_ls)
len_end_ls = len(end_ls)
mark = []

end_p = 0
curr = None
for item in start_ls:
    if end_p < (len_end_ls):
        if item == end_ls[end_p]:
            end_p += 1
            mark.append(0)
            curr = item
        else:
            if curr is not None:
                if item > curr:
                    mark.append(1)
                else:
                    mark.append(2)
            else:
                mark.append(1)
    else: 
        if curr is not None:
            if item > curr:
                mark.append(1)
            else:
                mark.append(2)
        else:
            mark.append(1)
        
if end_p < (len_end_ls):
    print(-1)
else:
    end_p = 0
    curr = None
    end_ls = end_ls[::-1]
    mark = mark[::-1]
    for idx, item in enumerate(start_ls[::-1]):
        if end_p < (len_end_ls):
            if item == end_ls[end_p]:
                end_p += 1
                curr = item
            else:
                if curr is not None:
                    if item < curr:
                        mark[idx] = 2
        else: 
            if curr is not None:
                if item < curr:
                    mark[idx] = 2
    mark = mark[::-1]
    
    if y*k >= x:
        smite = True
    else:
        smite = False

    segments = []
    segment = [0,True]
    for idx, item in enumerate(mark):
        if item != 0:
            segment[0] += 1
            if item == 1:
                segment[1] = False
        elif item == 0:
            if segment[0] != 0:
                segments.append(segment)
            segment = [0,True]

    if segment[0] != 0:
        segments.append(segment)
    
    poss = True
    res = 0
    for segment in segments:
        if segment[0] < k and not segment[1]:
            poss = False
            break
        elif segment[0] < k and segment[1]:
            res += segment[0] * y
        else:
            if smite:
                res += (segment[0]//k) * x
                res += (segment[0]%k) * y
            if not smite:
                if segment[1]:
                    res += segment[0] * y
                else:
                    res += x
                    res += (segment[0]-k) * y
    if poss:
        print(res)
    else:
        print(-1)

