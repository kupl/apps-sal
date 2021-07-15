n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
answer=[0]
students=[a[0]]
for i in range(1,n):
    students.sort(reverse=True)
    time=m-sum(students)
    counter=0
    for item in students:
        if time>=a[i]:
            answer.append(counter)
            break
        else:
            counter+=1
            time+=item
    else:
        answer.append(counter)
    students.append(a[i])
print(*answer)
        
    
    

