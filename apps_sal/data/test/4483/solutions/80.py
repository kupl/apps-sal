possesion=int(input())
cake=int(input())
donut=int(input())

remain_1=possesion-cake
remain_2=remain_1-(remain_1//donut)*donut

print(remain_2)
