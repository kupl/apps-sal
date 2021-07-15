#binary search reconstructure
  

def BinarySearch(my_list,key):
    l = 0
    r = len(my_list)- 1 
    #print(l,r)
    while r > l :
        mid = (l+r)//2
        if my_list[mid+1] <= key :
            l = mid + 1  
        else :
            r = mid   
        #print(l,r)
    return l

def weather_can_buy(day,total,req_list,sale_days):
    tmp_buy = []
    last_day = []
    # money = day
    # bug anything that is on sale
    d = day
    my_total = total
    for i in range(len(req_list)) : 
        last_day.append(0)
    for i in range(d):
        tmp_buy.append(0)    
    for i in range(len(sale_days)) : 
        if len(sale_days[i]) > 0 : 
            index = BinarySearch(sale_days[i],day)
            last_day[i] = sale_days[i][index]
    for i in range(len(last_day)) :
        if last_day[i]-1 > -1 :
            tmp_buy[last_day[i]-1] += req_list[i]
    # buying
    money = 0
    for i in range(d):
        money += 1
        my_total -= min(money,tmp_buy[i])
        money -= min(money,tmp_buy[i])        
    if my_total < 0 :
        return True
    elif money >= my_total * 2:
        return True
    else :
        return False
    
def function():
    tmp = input().split(" ")
    n = int(tmp[0]) # The number of type
    m = int(tmp[1]) 
    req_list = input().split(" ")
    req_list = list(map(int,req_list)) 
    total = sum(req_list)
    sale_days = []
    # sale days for acceleration
    for i in range(len(req_list)):
        sale_days.append([0])  
    for i in range(m) :
        tmp = input().split(" ")
        dj,tj = (int(tmp[0]),int(tmp[1]))
        sale_days[tj-1].append(dj)
    for i in range(len(sale_days)) :
        sale_days[i] = sorted(sale_days[i])
    # optimized by sorting
    for i in range(len(sale_days)) :
        sale_days[i] = sorted(sale_days[i])     
    #day = 0

    l = 1
    r = 2*total
    while r > l :
        mid = (l+r)//2
        if weather_can_buy(mid,total,req_list,sale_days) :
            r = mid
        else :
            l = mid + 1 
    print(r)
    
function()

