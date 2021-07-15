#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    n,m = input().split()
    maxminmex = int(n)
    for item  in range(int(m)):
        li, ri = input().split()
        maxminmex = min(maxminmex,int(ri)-int(li)+1)
       
    print(maxminmex)

    for i in range(int(n)):
        print(i % maxminmex)

def __starting_point():
    main()

__starting_point()
