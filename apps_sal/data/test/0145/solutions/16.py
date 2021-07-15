import math
import sys
def boyorgirl():
    distinct = []
    
    #Takes input
    datain = input()

    #Finds distinct chars
    for i in datain:
        if i not in distinct:
            distinct.append(i)
            
    #Determine boy or girl
    if len(distinct)%2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


boyorgirl()

