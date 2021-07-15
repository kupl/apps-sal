h,w = map(int,input().split())
n = int(input())
A = [int(i) for i in input().split()]
dic = {}
for i in range(n):
    dic[i+1] = A[i]

Map = [0 for i in range(h*w)]
height = 0
width = 0
now = 0
color = list(dic.keys())

color_num = 0
while now < h*w:
    if height%2==0:
        Map[now] = color[color_num]
        dic[color[color_num]] -= 1
        if dic[color[color_num]]==0:
            color_num += 1
        width += 1
        if width==w:
            height += 1
            width = w-1
    else:

        Map[now] = color[color_num]
        dic[color[color_num]] -=1
        if dic[color[color_num]]==0:
            color_num += 1
        width -= 1
        if width==-1:
            height += 1
            width = 0
    now = height*w + width
st = 0

for i in range(h):
    print(*Map[st:st+w])
    st = st+w
