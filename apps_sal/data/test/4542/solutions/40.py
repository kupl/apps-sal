#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-10-09 16:08:34 +0900
# LastModified: 2020-10-09 16:19:59 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from itertools import groupby


def main():
    S = input()
    sgroup = groupby(S)
    for cnt, (key, group) in enumerate(sgroup):
        pass
    print(cnt)






def __starting_point():
    main()

__starting_point()
