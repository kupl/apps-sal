#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-26 23:24:58 +0900
# LastModified: 2020-09-26 23:33:37 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    L = input()
    if int(L[0]) + int(L[1]) + int(L[2]) + int(L[3]) == 7:
        print(("{}+{}+{}+{}=7".format(L[0], L[1], L[2], L[3])))

    elif int(L[0]) + int(L[1]) + int(L[2]) - int(L[3]) == 7:
        print(("{}+{}+{}-{}=7".format(L[0], L[1], L[2], L[3])))

    elif int(L[0]) + int(L[1]) - int(L[2]) + int(L[3]) == 7:
        print(("{}+{}-{}+{}=7".format(L[0], L[1], L[2], L[3])))

    elif int(L[0]) - int(L[1]) + int(L[2]) + int(L[3]) == 7:
        print(("{}-{}+{}+{}=7".format(L[0], L[1], L[2], L[3])))

    elif int(L[0]) + int(L[1]) - int(L[2]) - int(L[3]) == 7:
        print(("{}+{}-{}-{}=7".format(L[0], L[1], L[2], L[3])))

    elif int(L[0]) - int(L[1]) + int(L[2]) - int(L[3]) == 7:
        print(("{}-{}+{}-{}=7".format(L[0], L[1], L[2], L[3])))

    elif int(L[0]) - int(L[1]) - int(L[2]) + int(L[3]) == 7:
        print(("{}-{}-{}+{}=7".format(L[0], L[1], L[2], L[3])))

    elif int(L[0]) - int(L[1]) - int(L[2]) - int(L[3]) == 7:
        print(("{}-{}-{}-{}=7".format(L[0], L[1], L[2], L[3])))




def __starting_point():
    main()

__starting_point()
