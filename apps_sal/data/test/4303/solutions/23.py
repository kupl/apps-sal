n,k=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]

# ==================================================-
# 二分探索
# functionを満たす,search_listの最大の要素を出力
# 【注意点】searchリストの初めの方はfunctionを満たし、後ろに行くにつれて満たさなくなるべき
import math
import sys
sys.setrecursionlimit(10**9)
def binary_research(start,end,function):
    if start==end:
        return start
    middle=math.ceil((start+end)/2)
    if function(middle):
        start=middle
    else:
        end=middle-1
    return binary_research(start, end, function)
positive=[]
negative=[]
zero=False


for i in x:
    if i<0:
        negative.append(abs(i))
    elif i>0:
        positive.append(i)
    else:
        zero=True
positive.sort()
negative.sort()


def function(time):
    if time==-1:
        return True
    ans_list=[]
    ans=0
    if zero:
        ans+=1
    for i in positive:
        if i<=time:
            ans_list.append(i)
            ans+=1
        else:
            break
    negative_list=[]
    for i in negative:
        if i<=time:
            negative_list.append(i)
        else:
            break
    negative_list=negative_list[::-1]
    newans=ans
    while negative_list:
        newans,ans_list,negative_list=function2(ans_list,negative_list,newans,time)
        ans=max(ans,newans)
        if ans_list==[]:
            break
        else:
            ans_list.pop()
            newans-=1
    if ans>=k:
        return False
    return True



def function2(ans_list,negative_list,ans,time):
    if ans_list==[]:
        max_num=0
    else:
        max_num=ans_list[-1]
    remain_time=time-max_num*2
    while negative_list:
        i=negative_list.pop()
        if max_num==0:
            if i<=remain_time:
                ans+=1
        elif max_num+i+min(i,max_num)<=time:
            ans+=1
        else:
            negative_list.append(i)
            break
    return ans,ans_list,negative_list


print(binary_research(-1,3*10**8+1,function)+1)
