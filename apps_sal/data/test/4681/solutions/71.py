#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    numbers=[2,1]
    number = int(input())

    for i in range(2,number+1):
        numbers.append(numbers[i-1]+numbers[i-2])
    print(numbers[-1])
    
def __starting_point():
    main()
__starting_point()
