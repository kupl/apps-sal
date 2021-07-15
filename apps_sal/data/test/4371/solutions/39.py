#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def ngram(data,n):
    return [data[i:i+n] for i in range(len(data))]

def main():
    s = input().rstrip()
    datas=ngram(s,3)
    answers=[]
    
    for data in datas:
        answers.append(abs(753-int(data)))
    print(min(answers))

def __starting_point():
    main()
__starting_point()
