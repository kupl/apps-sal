#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 20:07:20 2018

@st0rmbring3r
"""

word = input()
while word == word[::-1] and len(word)>0:
    word = word[:-1]

print(len(word))
