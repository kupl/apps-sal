FROM ubuntu:20.04

ARG USERNAME=apps

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        python3 \
        python3-pip \
        ssh-client \
        sudo && \
    apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir \
        autopep8 \
        pylint 

RUN useradd \
        --shell $(which zsh) \
        -G sudo \
        -m -d /home/${USERNAME} -k /etc/skel \
        ${USERNAME} && \
    sed -i -e 's/%sudo.*/%sudo\tALL=(ALL:ALL)\tNOPASSWD:ALL/g' /etc/sudoers
