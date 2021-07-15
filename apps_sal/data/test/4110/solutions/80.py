D, G = map(int, input().split())
PC = [list(map(int, input().split())) for i in range(D)]


points = []
patterns = []
    
def flagfun(flag):
    if len(flag) == D:
        patterns.append(flag)
        return
    
    flagfun(flag+'0')
    flagfun(flag+'1')
    
def index_pattern():
    flagfun('')
    idxes = []
    for pattern in patterns:
        tmp_idx = []
        for idx, flag in enumerate(pattern):
            if flag == '1':
                tmp_idx.append(idx)
        idxes.append(tmp_idx)
    return idxes

def culc_points():
    for i, scores in enumerate(PC):
        max_score = (i+1)*scores[0]*100 + scores[1]
        points.append([scores[0], max_score])

culc_points()

idxes = index_pattern()
count = 1000000

for idx in idxes:
    tmp_count = 0
    tmp_score = 0
    remain_idx = [i for i in range(D)]
    for i in idx:
        tmp_count += points[i][0]
        tmp_score += points[i][1]
        num_index = remain_idx.index(i)
        remain_idx.pop(num_index)
           
    if tmp_count >= count:
        continue
    
    if tmp_score >= G:
        count = tmp_count
        continue
    
    max_idx = remain_idx.pop(-1)
    for i in range(1, points[max_idx][0]):
        tmp_count += 1
        tmp_score +=(max_idx+1)*100
        if tmp_count >= count:
            break
            
        if tmp_score >= G:
            count = tmp_count
            break

print(count)
