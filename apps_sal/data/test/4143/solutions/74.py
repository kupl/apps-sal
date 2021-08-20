"""
people_num=int(input(''))
time_sum=0
num_trans=[]

for i in range(5):
    num_trans.append(int(input('')))

location=[[people_num,0,0,0,0,0]]

while location[0][5]<people_num:
    location_old=location.pop(0)
    print(location_old)
    location_new=[0,0,0,0,0,location_old[5]]
    print("step0")
    for i in range(5):
        if location_old[i]>num_trans[i]:
            location_new[i+1]+=num_trans[i]
            location_new[i]+=location_old[i]-num_trans[i]
        else:
            location_new[i+1]+=location_old[i]
    time_sum+=1
    location.append(location_new)
    print("step2")
print(str(time_sum))

↑失敗version
"""
import math
'\n解説\n\n最も通りにくい、つまり容量が最も小さい交通機関を考えます。直感的には、最短時間で移動する場\n合でも、1 分でたどり着けるのは 𝑋 人 (交通機関の容量の最小を 𝑋 とする) になります。これは、「1\n秒に 15 L のペースで水を送れるポンプと、1 秒に 12 L のペースで水を送れるポンプをつなげたときに、\n1 秒に送れる水の量は小さい方を取って 12 L」 になるのと同じ原理です。\nつまり、先ほどの貪欲的な方法ではなくて、1 分に 𝑋 人ずつ 1 つ先に進めてやっても、直感的には\nかかる時間は変わらなさそうです。また、移動時間は 「(𝑁 ÷ 𝑋 を切り上げた値) + 4 分」 と、簡単に\n計算できるようになります。\n'
people_num = int(input(''))
num_trans = []
for i in range(5):
    num_trans.append(int(input('')))
print(math.ceil(people_num / min(num_trans) + 4))
