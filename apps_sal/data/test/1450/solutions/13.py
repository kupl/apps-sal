s = str(input())

answer = []


ed_count = 0
prev_null = 0

prev_twos = 0
for el in s:
    if el == "1":
        ed_count += 1
    else:
        if el == "0":
            if prev_null == 0:
                if prev_twos!=0:
                    answer.append([2, prev_twos])
                    prev_twos = 0

            prev_null +=1
        else:
            if prev_twos == 0:
                if prev_null!=0:
                    answer.append([0, prev_null])
                    prev_null = 0
                    
            prev_twos +=1
    


if prev_twos!=0:
    answer.append([2, prev_twos])
    prew_twos = 0

if prev_null!=0:
    answer.append([0, prev_null])
    prev_null = 0

if len(answer) !=0 and answer[0][0] == 0:
    print("{}".format(answer[0][0]) * answer[0][1], end = '')

print("1"*ed_count, end = "")
z = len(answer)
min_in = 0
if z!= 0 and answer[0][0] == 0:
    min_in += 1
for i in range(min_in, z):
    print(str(answer[i][0]) * answer[i][1], end = "")
            

