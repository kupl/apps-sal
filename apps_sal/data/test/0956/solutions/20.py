N, part = list(map(int, input().split())) 

part /= 100 

data = dict() 

for i in range(N): 
    fr1, fr2 = list(map(int, input().split())) 

    if fr1 in data: 
        data[fr1].add(fr2) 
    else: 
        data[fr1] = set() 
        data[fr1].add(fr2) 
 
    if fr2 in data: 
        data[fr2].add(fr1) 
    else: 
        data[fr2] = set() 
        data[fr2].add(fr1) 

answer = [] 

for i in list(data.keys()): 
    res = [] 
    for j in list(data.keys()): 
        if i != j and i not in data[j]: 
            com_fr = data[i] & data[j] 
       #     print(len(data[i]) * part, len(com_fr) / len(data[i])) 
            if part <= len(com_fr) / len(data[i]): 
             #   if len(com_fr) != 0: 
                res.append(j) 
    
    answer.append((i, ": ", len(res), ' ', ' '.join(map(str, sorted(res))))) 

answer.sort(key = lambda x: int(x[0]))

for i in range(len(answer)): 
    print(''.join(map(str, answer[i]))) 

