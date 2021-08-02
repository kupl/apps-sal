
all_input = []  # appendのために宣言が必要
while True:
    try:
        all_input.append(list(map(int, input().split())))
    except:
        break;
        # または、return,os.returnをして止める。

N, M = all_input[0][0], all_input[0][1]
p = all_input[-1]
all_input.pop(0), all_input.pop(-1)
switch = [all_input[i][1:] for i in range(M)]
num_switch = [all_input[i][0] for i in range(M)]

all_on = 0
for i in range(2**N):
    num_light_on = 0  # M個の電球のうち，点灯するものの個数をincrementする
    for m in range(M):
        switch_on = 0
        for j in range(N):
            if (i >> j) & 1:
                if j + 1 in switch[m]:
                    switch_on += 1
        if switch_on % 2 == p[m]:
            num_light_on += 1
    if num_light_on == M:
        all_on += 1
print(all_on)
